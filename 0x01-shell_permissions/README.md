SHELL PERMISIONS
su  to give betty superuser right
id -un prints the effective username of the current user
id -G prints the effective username of the current user
chown changes the owner of the file
touch creates an empty file called
chmod u+x adds execute permission to the owner of the file
chmod u+x g+x o+r adds execute permission to the owner and the group owner, and read permission to other users, to the file
chmod ugo+x adds execution permission to the owner, the group owner and the other users, to the file
chmod 007 sets all permissions to only others
chmod 753 sets mode to -rwxr-x-wx
chmod --reference=olleh hello set the mode of hello to olleh
chmod –R ugo+X .  adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users
mkdir –m 751 my_dir   creates a directory called my_dir with permissions 751 in the working directory.
chgrg changes the group owner
chown –hR vincent staff .   changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
chown –h vincent staff _hello    changes the owner and the group owner of _hello to vincent and staff respectively
chown --from=guillaume betty hello   changes the owner of the file hello to betty only if it is owned by the user guillaume
telne towel.blinkenlights.nl   will play the StarWars IV episode in the terminal

