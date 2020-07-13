# deploy_dataScienceModel_docker_flask
## how to use the project :

1-install docker and docker-compose in your computer (google)

2- pull th project (**web repository and docker-compose.xml file  must be in the same directory**)

3- run the docker commands: ***docker-compos build***, ***docker-compose up -d***

4-take your predictions from url ***127.0.0.1:5000*** (or from another sever wich can ping your IP adress) 
## NB:
the objective here is to deploy the model and not to build it, the construction phase is assumed to be known (jupyter notebook), in this project the model is saved in pkl format (linear_regression_model.pkl)