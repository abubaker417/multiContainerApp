# Create network
docker network create appnet

# Build backend
cd backend
docker build -t backend .

# Run backend on network
docker run -td --network appnet --name backend backend

# Build frontend
cd backend
docker build -t frontend .

# Run frontend on network
docker run -td --network appnet --name frontend frontend

# Port forward
docker run -td -p 8000:8000 --network appnet --name frontend frontend
