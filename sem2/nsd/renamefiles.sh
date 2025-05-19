pid=$$
for file in *
do
    if [ -f "$file" ]; then
        mv "$file" "$file.$pid"
        echo "Renamed $file to $file.$pid"
    fi
done

