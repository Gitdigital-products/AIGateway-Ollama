FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY . .
RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux go build -o aigateway-ollama

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/aigateway-ollama .
COPY --from=builder /app/.env.example .env

EXPOSE 8080
CMD ["./aigateway-ollama"]
