# Install Docker
If Docker is not installed on your computer, go to https://www.docker.com/products/docker-desktop/ and install docker for your operating system.
Once docker is installed, run `docker version` to test if the installation was properly done. You should see a bunch of details about your version of docker.
# Instruction to run the application
- Download the code from 
- Go at the root of the repository directory. The code has been dockerized. To run the application:
    - Build the docker image
        - You can decide to enable logging by specifying a `--build-arg ENV=[production|development]` in the docker build command
            - To enable logging,  run `docker image build --build-arg ENV=development -t hello-world .`
            - To disable logging,  run `docker image build --build-arg ENV=development -t hello-world .` or `docker image build -t hello-world .`
    - Run the docker image
        - Run (A) `docker run -p 5000:5000 --name hello_world -it hello-world` to run the docker image
        - If you encounter the following error message "docker: Error response from daemon: Conflict. The container name "/hello_world" is already in use by container". Run `docker rm hello_world` and rerun the command (A)
        - At this point, the application is running
    - To run the unit tests on the application
        - Run `docker exec hello_world python -m unittest discover -v` in another terminal window if the docker image is running
        - If there is no docker image running, you can run `python -m unittest discover -v` from the root of the directory

    - To send requests to the application, run the following command
        - on macos
            - Run `curl http://localhost:5000` in the terminal to test the GET request on `/`
            - Run `curl http://localhost:5000 -H 'Accept: application/json'` in the terminal to test the GET request on `/`
            - Run `curl -X POST http://localhost:5000/ -H 'Content-Type: application/json' -d '{"name":"john doe"}'` in the terminal for the POST request on `/`
    - To stop the application
        - on Windows
            - Run `Remove-item alias:curl`
            - Run `curl http://localhost:5000` in the terminal to test the GET request on `/`
            - Run `curl http://localhost:5000 -H 'Accept: application/json'` in the terminal to test the GET request on `/`
            - Run `curl -X POST http://localhost:5000/ -H 'Content-Type: application/json' -d '{"name":"john doe"}'` in the terminal for the POST request on `/`
    - To stop the application
        - Press `cmd+c` or `ctrl+c`
        - Run `docker rm hello_world`
        - Stop docker