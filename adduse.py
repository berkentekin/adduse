import os
pkgname = input("Type package name: ")

root = '/var/db/repos/gentoo'

for category in os.listdir(root):
    try:
        for item in os.listdir(f"{root}/{category}"):
            if pkgname == item:

                flags = input("Type flag(s): ")
                conffile = f'/etc/portage/package.use/{pkgname}'

                if os.path.isfile(conffile):
                    args = f" {flags}"
                else:
                    args = f"{category}/{item} {flags}"

                with open(conffile, 'a+') as f:
                    if input("Are you sure (y/n)? ").lower() == 'y':
                        f.write(args)
                        f.flush()
                        f.seek(0)
                        print("\nHere are the contents of the file:")
                        print(f.read())

                    else:
                        print('\nNo action has been taken.')
                        print(f.read())
                    f.close()


                exit()
    except NotADirectoryError:
            continue
raise Exception("Package not found.")
