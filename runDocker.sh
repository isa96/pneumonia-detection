xhost +local:docker 
XSOCK=/tmp/.X11-unix 
XAUTH=/tmp/.docker.xauth 
touch $XAUTH 
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -
docker run -it --rm --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="$XSOCK:$XSOCK:rw" --device=/dev/video0:/dev/video0 clayrisee/pneumonianet:latest 
xhost -local:docker