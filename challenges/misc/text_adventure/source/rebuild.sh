sudo docker build . -t textadventure
sudo docker run --rm --privileged -p 1976:1976 textadventure
