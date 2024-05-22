#!/bin/bash -x

WD=$(dirname $0)
CONF=$WD/etc/aptly-ntrepo.conf
ARCHS="amd64,arm64,armhf"
PREFIX="ubuntu"
APTLY="aptly -config=$CONF"
REPOS="18.04 20.04 22.04"

declare -A OSNAME
OSNAME[18.04]="bionic"
OSNAME[20.04]="focal"
OSNAME[22.04]="jammy"

declare -A DIST_RELEASE
DIST_RELEASE[18.04]="1804"
DIST_RELEASE[20.04]="2004"
DIST_RELEASE[22.04]="2204"

export GNUPGHOME=$WD/keys/gnupg

function Do
{
    local cmd="$@"
    echo $cmd
    if [ "$DRYRUN" == "" ]; then
        $cmd
        if [[ $? -ne 0 ]]; then
            exit 1
        fi
    fi
}

#запускаю по крону первого числа каждого месяца
function create_stable_snapshot 
{
#   source ${TOPDIR}/distribution/variables
    echo "GNUPGHOME: $GNUPGHOME"
#    DATA_CREATE_SHOT=$(date +%F-%H%M)
    DATA_CREATE_SHOT=$(date +%Y-%m-01-%H%M)
    for repo in $REPOS; do
        NAME_PUBLISH_SNAPSHOT=ubuntu-$repo-stable-$DATA_CREATE_SHOT
        Do $APTLY snapshot create $NAME_PUBLISH_SNAPSHOT from repo ubuntu-$repo-devel 
        Do $APTLY publish switch -gpg-key="35C973B37899FF01E608C2A23033181FBDDAED3C" -architectures=$ARCHS -component="main" stable ubuntu/$repo $NAME_PUBLISH_SNAPSHOT
    done
}

function add_devel_packets_in_stable()
{   
# имена пакетов для добавления в stable snapshot
    TOPDIR=${PWD}
         
    NP_1804=$(sed '1q;d' ./name_packets)
    NP_2004=$(sed '2q;d' ./name_packets)
    NP_2204=$(sed '3q;d' ./name_packets)
    source ./variables

    echo "GNUPGHOME: $GNUPGHOME"
    DATA_CREATE_SHOT=$(date +%F-%H%M)
    for repo in $REPOS; do
        NAME_PUBLISH_SNAPSHOT="ubuntu-$repo-scandidat-$DATA_CREATE_SHOT"
        STABLE_SNAPSHOT=$(Do $APTLY snapshot list | grep $(date +%Y-%m-01) | grep "ubuntu-$repo-stable" | cut -d "]" -f 1 | cut -d "[" -f 2 | tail -1 | cut -d "_" -f 1)
        echo STABLE_SNAPSHOT $STABLE_SNAPSHOT
#3
        Do $APTLY snapshot create $NAME_PUBLISH_SNAPSHOT from repo ubuntu-$repo-devel  #тут все верно на 2 этапе создаем снапшот с devel repo        
#4
        NAME_PCK="NP_${DIST_RELEASE[$repo]}"
        # Команда eval сопоставляет значения из одной или нескольких переменных.
        NUMBER_ADDED_PCK=$(eval echo \${$NAME_PCK})
        for NAME_PACKG in "$NUMBER_ADDED_PCK"; do
            NUMBER_ADDED_PACKG=$(Do $APTLY snapshot list | grep "$(date +%Y-%m-01)" | grep "ubuntu-$repo-stable" | cut -d "]" -f 1 | cut -d "[" -f 2 | cut -d "_" -f 2 | sed 's/^p//' | sort -n | tail -1)
            if [[ $NUMBER_ADDED_PACKG =~ ^[0-9] ]]; then
                echo номер добавляемого пакета найден
                ADDENDUM_NUMBER=$NUMBER_ADDED_PACKG
                ((ADDENDUM_NUMBER++))
                Do $APTLY snapshot pull -architectures=amd64,arm64,armhf -no-remove $STABLE_SNAPSHOT\_p$NUMBER_ADDED_PACKG $NAME_PUBLISH_SNAPSHOT $STABLE_SNAPSHOT\_p$ADDENDUM_NUMBER $NAME_PACKG           
            else  
                echo номер добавляемого пакета не найден
                ADDENDUM_NUMBER=1
                Do $APTLY snapshot pull -architectures=amd64,arm64,armhf -no-remove $STABLE_SNAPSHOT $NAME_PUBLISH_SNAPSHOT $STABLE_SNAPSHOT\_p$ADDENDUM_NUMBER $NAME_PACKG           
            fi
        done  
#5
        Do $APTLY publish switch -gpg-key="35C973B37899FF01E608C2A23033181FBDDAED3C" -architectures=$ARCHS -component="main" stable ubuntu/$repo $STABLE_SNAPSHOT\_p$ADDENDUM_NUMBER
    done
}

#запускаю по крону первого числа каждого месяца после выполнения create_stable_snapshot 
function remove_snapshot_scandidat
{
    for REPO in $REPOS; do 
        stable_snapshot=$(Do $APTLY snapshot list | grep $(date +%Y-%m-01) | grep ubuntu-$REPO-stable | cut -d "]" -f 1  | cut -d "[" -f 2  | awk 'FNR>1')
#для вычищения нечести   stable_snapshot=$(Do $APTLY snapshot list |  grep ubuntu-$REPO-stable-2024-05-20 |  cut -d "]" -f 1  | cut -d "[" -f 2   ) 
        scandidat_snapshot=$(Do $APTLY  snapshot list | cut -d ":" -f1 | grep ubuntu-$REPO-scandidat | cut -d "]" -f 1  | cut -d "[" -f 2)
        #удаляем stable_snapshot
        if [[ -n $stable_snapshot ]]; then
            for rm_stable_snapshot in $stable_snapshot; do
                Do $APTLY snapshot drop -force $rm_stable_snapshot
            done
        fi

        if [[ -n $scandidat_snapshot ]]; then
            #удаляем scandidat_snapshot
            for rm_scandidat_snapshot in $scandidat_snapshot; do
                Do $APTLY snapshot drop -force $rm_scandidat_snapshot
            done
        fi
     done
}


while [[ "$#" -gt 0 ]]; do
#    OS=$2
#    if [[ $OS == "" ]]; then
#        echo "Укажите ОС: ubuntu2204    ubuntu2004    ubuntu1804"
#    fi
    case $1 in
        create-stable-snapshot)
            create_stable_snapshot
            exit 0 ;;

         remove-snapshot-scandidat)
            remove_snapshot_scandidat
            exit 0 ;;    

        add-devel-packets-in-stable)
            add_devel_packets_in_stable
            exit 0 ;;
            
        *) echo "Не известный параметр: $1"; exit 1 ;;
    esac
done
