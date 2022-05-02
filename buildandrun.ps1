cd "C:\dev\webgarden"
docker build -t webgarden .
cd "C:\dev\webgarden"
docker run -it --rm --name webgarden-server webgarden -p 8699:8000