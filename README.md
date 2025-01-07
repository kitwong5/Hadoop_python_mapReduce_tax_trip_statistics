Assumption: Trips.txt, Taxis.txt, hadoop-streaming-3.1.4.jar already available to user

Setup Steps:
1) use WinSCP to transfer follow files from your PC to jumphost /home/ec2-user/data/ </br>
	hadoop-streaming-3.1.4.jar</br>
	mapper_t1.py</br>
	reducer_t1.py</br>
	Task1-run.sh</br>

2) use Putty to login the jumphost sever
3) run follow script to create cluster
4) copy file to cluster from jumphost
5) login to cluster
	
Run Steps:
1) run follow script to grant execution right to the shell script</br>
	chmod +x Task1-run.sh
2) run follow script to execute task 1</br>
	./Task1-run.sh
3) run follow script to check execution output</br>
	hadoop fs -ls /Output/Task1</br>
	hadoop fs -cat /Output/Task1/part-00000</br>
	hadoop fs -cat /Output/Task1/part-00001</br>
	hadoop fs -cat /Output/Task1/part-00002</br>
