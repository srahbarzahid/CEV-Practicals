read -p "Enter the filename: " filename
if [ ! -f "$filename" ]; then
    echo "File $filename does not exist."
    exit 1
fi
sed -i '/linux/I d' "$filename"
echo "All lines containing the word 'linux' have been deleted."

# temp_file=$(mktemp)
#while IFS= read -r line; do
#    if [[ ! "$line" =~ linux ]]; then
#        echo "$line" >> "$temp_file"
#   fi
# done < "$filename"
#mv "$temp_file" "$filename" 
