echo	#for new line
echo	#for new line
echo "This is load testing of Server"
echo "Below sending 1000 request , 10 at a time to server"
echo	#for new line
echo	#for new line

#below command is for sending 1000 requests , 10 at a time to server
ab -n 1000 -c 10 http://127.0.0.1:$1/

echo	#for new line
echo	#for new line

echo "sucessfully completed 1000 request , 10 at a time to server"

sleep 5


echo	#for new line
echo	#for new line
echo "Below sending 10000 request , 100 at a time to server"
echo	#for new line
echo	#for new line


ab -n 10000 -c 100 http://127.0.0.1:$1/

echo	#for new line
echo	#for new line

echo "sucessfully completed 10000 request , 100 at a time to server"
echo "Load testing completed..."

