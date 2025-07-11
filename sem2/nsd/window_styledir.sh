read -p "Enter the directory path: " dir
if [ ! -d "$dir" ]; then
    echo "Directory $dir does not exist."
    break
fi
echo "Directory listing for $dir:"
ls -1 "$dir"


