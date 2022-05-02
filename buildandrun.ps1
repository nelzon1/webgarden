cd "C:\dev\webgarden"
docker build -t webgarden .
cd "C:\dev\webgarden"
docker run -it -p 8600:8000 --rm --name webgarden-server webgarden