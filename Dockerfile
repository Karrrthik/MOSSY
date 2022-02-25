FROM alpine
WORKDIR /app
COPY ["./mossy/package.json", "./mossy/package-lock.json", "./"]
RUN npm install
COPY . .
ENV PORT=8003
EXPOSE 8003
CMD ["npm", "start"]