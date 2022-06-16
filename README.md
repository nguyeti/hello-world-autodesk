# Hello-world-autodesk
## Prerequisite 
### Docker 
If Docker is not installed on your computer, go to https://www.docker.com/products/docker-desktop/ (MacOS and Windows), download the installation file for your operating system.
Once the download is finished, click on the executable and follow the installation wizard.
Once docker is installed, open a terminal and run `docker version` to test if the installation was properly done. You should see some information about the installed docker version.
You may need to restart your computer during the installation process.

### Git
You will need git during this process.
- OSX: open a terminal and run `brew install git` and `git --version` to check your installation
- Windows: go to [this](https://git-scm.com/download/win) website, download the installer and install git. Open git bash and run `git --version` to check that git is properly installed.

## Instruction to run the application
- Open a terminal (OSX) or git bash (windows), and clone the source code by running `git clone https://github.com/nguyeti/hello-world-autodesk.git`
- Change directory to `hello-world-autodesk` by running `cd hello-world-autodesk`
- You should now be in the root of the repository directory. The code has been dockerized. To run the application, open the powershell (windows) or terminal (OSX) and run the following commands:
    - Start the Docker daemon
    - Build the docker image
        - The logging is only enabled in the development environment 
            - To enable logging,  run `docker image build --build-arg ENV=development -t hello-world .`
            - Otherwise, run `docker image build -t hello-world .`
    - Run the docker image
        - Run (A) `docker run -p 5000:5000 --name hello_world -it hello-world` to run the docker image
            - If you encounter the following error message "docker: Error response from daemon: Conflict. The container name "/hello_world" is already in use by container" 
                - Run `docker rm hello_world` and rerun the command (A)
            - If the port `5000` is already taken on your computer, you can change the port. e.g. `docker run -p <port_of_your_choice>:5000 --name hello_world -it hello-world`
        - At this point, the application is running
    - To run the unit tests on the application
        - Run `docker exec hello_world python -m unittest discover -v` in another terminal window if the docker image is running
        - If there is no docker image running, you can run `python -m unittest discover -v` from the root of the directory
    - To send requests to the application, run the following curl command
        - If you changed the port number in the previous step, replace `5000` in the following commands with the port you chose
        - If you are using mac, open the terminal in the root of the folder `hello-world-autodesk`. If you are using windows, go in the folder `hello-world-autodesk` in your file explorer then right click and select "open git bash here"
        - curl commands:
            - Run `curl http://localhost:5000` to test the GET request on `/`
            - Run `curl http://localhost:5000 -H 'Accept: application/json'` to test the GET request on `/`
            - Run `curl -X POST http://localhost:5000/ -H 'Content-Type: application/json' -d '{"name":"john doe"}'` for the POST request on `/`
    - To stop the application
        - Press `cmd+c` or `ctrl+c` in the terminal window where the docker image has been run
        - Run `docker ps` and run `docker stop <container_id>` on the image you want to stop
        - Run `docker rm hello_world`
        - Shut down docker