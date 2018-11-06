# Tweet Analysis Appliation for Kubernetes / PKS
A sample multi-tier application to process Twitter feed and stream into a KAFKA topic and perform analysis with Jupyter NB.

## Objective
To provide a simple to deploy sample or demo application showing Big Data (Kafka and Spark) in real workd scenario.

## Prerequisites
A running Kubernetes cluster.


## Installation

Pull down the Repo to a machine that has access to your Kubernetes cluster.



## Example

	### Calling the Library

		import marathon-client


	### Initialize a Marathon Connection Object -

		new_marathon = marathon-client.Marathon(dcos_master,dcos_auth_token)

	### Get All Marathon Apps -

		apps = new_marathon.get_all_apps()


	### Get Marathon App Details -
		marathon_app = '/dev/nginx01'
		app_details = aws_marathon.get_app_details(marathon_app)

	### Scale Marathon App -
		new_marathon.scale_app(marathon_app, instances)

	### Add Marathon Application -
		marathon_app_json_file = '/Users/tkraus/sandbox/marathon/12b-siege.json'
		new_app = new_marathon.add_app(marathon_app_json_file)