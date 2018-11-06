# Tweet Analysis Appliation for Kubernetes / PKS
A sample multi-tier application to process Twitter feed and stream into a KAFKA topic and perform analysis with Jupyter NB.

## Objective
To provide a simple to deploy sample or demo application showing Big Data (Kafka and Spark) in real workd scenario.

## Prerequisites
A running Kubernetes cluster.


## Installation

    ### Pull down the Repo to a machine that has access to your Kubernetes cluster.
        git clone https://github.com/tkrausjr/tweet-analysis.git

    ###  Export the required Environment Variables
	export TWITTER_ACCESS_TOKEN=
	export TWITTER_ACCESS_TOKEN_SECRET=
	export TWITTER_CONSUMER_KEY=
	export TWITTER_CONSUMER_SECRET=
	export TWITTER_FILTER_STRING= <String to filter Tweets for producing to Kafka>
	export KAFKA_TARGET=   <Broker_IP : 9092>




## Example - Running locally with Docker-compose

    ### To run on a local workstation with docker-compose.
    	$ git clone https://github.com/wurstmeister/kafka-docker.git
	$ cd /kafka-docker/
	$ vi docker-compose-single-broker.yml
		Change - "KAFKA_ADVERTISED_HOST_NAME: xx.xx.xxx.xx  to the IP Address of your local workstation.
	$ docker-compose -f docker-compose-single-broker.yml up -d
	$ docker ps
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS                                                NAMES
c1d4d3e00cc2        wurstmeister/zookeeper   "/bin/sh -c '/usr/..."   About an hour ago   Up About an hour    22/tcp,2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp   kafkadocker_zookeeper_1
c7eb07462bd0        kafkadocker_kafka        "start-kafka.sh"         About an hour ago   Up About an hour    0.0.0.0:9092->9092/tcp                               kafkadocker_kafka_1
	Test with kafkacat
 	    $ kafkacat -P -b 91.11.122.21:9092 -t test	
	    	Enter text and CTL-C to stop
	     $ kafkacat -C -b 191.11.122.21:9092 -t test
	Run the Python Script 
		python3 tweet-producer.py  ## NEED TO TEST THIS FIRST Have been only running from PYCHARM.


	### Something next-

		something

	### Next  -

		something


