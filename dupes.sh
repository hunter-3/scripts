# Report those
for HASH in $POSSIBLEDUPES
do
        # Report a hash value with possible duplicates
        echo "Possible duplication for $DUPE"
        # Save the corresponding file names in FILELIST.
        grep $HASH $HASHLIST |
                sed 's/SHA256(//' |
                sed 's/)= .*//' |
                tee $FILELIST
        # Do pairwise comparisons with the corresponding files.
        # There are n files in the list.
        n=$(wc -l $FILELIST)
        # Outer loop: i = 1, ... n-1
        i=1
        while [ $i -lt $n ]
        do
                # Inner loop: j = i+1, ... n
                j=$(( $i + 1 ))
                while [ $j -le $n ]
                do
                        # Extract ith and jth files in list
                        FILE1="$(head -$i $FILELIST | tail -1)"
                        FILE2="$(head -$j $FILELIST | tail -1)"
                        # If cmp returns 0, files were identical
                        cmp -s "${FILE1}" "${FILE2}"
                        if [ $? == "0" ]
                        then
                                echo " IDENTICAL FILES:"
                                echo "   ${FILE1}"
                                echo "   ${FILE2}"
                        fi
                        j=$(( $j + 1 ))
                done
                i=$(( $i + 1 ))
        done

        echo ""

done

rm -f $HASHLIST $FILELIST
