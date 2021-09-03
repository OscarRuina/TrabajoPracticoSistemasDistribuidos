package com.unla.servidor.server;

import java.io.IOException;

import com.unla.servidor.service.UserService;

import io.grpc.Server;
import io.grpc.ServerBuilder;

public class GRPCServer {

    public static void main(String args[]) throws IOException, InterruptedException {

        Server server = ServerBuilder.forPort(9090).addService(new UserService()).build();

        server.start();

        System.out.println("Server started on " + server.getPort());

        server.awaitTermination();

    }
    
}
