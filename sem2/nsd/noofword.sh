file_path= "/home/student/Rahbar/temp.txt"
no_lines=`wc --lines < $file_path`
no_words=`wc --word < $file_path`
echo "Number of lines:"$no_lines
echo "Number of words:"$no_words 
