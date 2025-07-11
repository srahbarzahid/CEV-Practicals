read -p "Enter the first file: " file1
read -p "Enter the second file: " file2
if cmp -s "$file1" "$file2"; then
    echo "The files are identical. Deleting $file2..."
    rm "$file2"  
else
    echo "The files are different."
fi

