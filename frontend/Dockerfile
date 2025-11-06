# 1️⃣ Use Node.js base image
FROM node:20-alpine

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy package files
COPY package.json package-lock.json ./

# 4️⃣ Install dependencies
RUN npm install

# 5️⃣ Copy the rest of the frontend code
COPY ./src ./src

# 6️⃣ Expose port for Vite dev server
EXPOSE 5173

# 7️⃣ Start the frontend dev server
CMD ["npm", "run", "dev", "--", "--host"]
