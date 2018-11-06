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
        export
        export
        export
        export
        export
        export




## Example - Running locally with Docker-compose

	### Calling the Library

		import marathon-client


	### Initialize a Marathon Connection Object -

		new_marathon = marathon-client.Marathon(dcos_master,dcos_auth_token)

	### Get All Marathon Apps -

		apps = new_marathon.get_all_apps()


