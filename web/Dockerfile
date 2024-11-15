# Use the official Node.js image as the base image
FROM node:20

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and pnpm-lock.yaml to the working directory
COPY package.json pnpm-lock.yaml ./

# Install pnpm globally
RUN npm install -g pnpm

# Install rimraf globally
RUN npm install -g rimraf

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Install the application dependencies
RUN pnpm install

# Define the command to run the application
CMD ["pnpm", "start"]