package com.unla.servidor.service;

import com.unla.servidor.grpc.User;
import com.unla.servidor.grpc.userGrpc;

import io.grpc.stub.StreamObserver;

public class UserService extends userGrpc.userImplBase{

    @Override
    public void login(User.LoginRequest request, StreamObserver<User.APIResponse> responseObserver) {

        String username = request.getUsername();
        String password = request.getPassword();

        User.APIResponse.Builder response = User.APIResponse.newBuilder();

        if(username.equals(password)){
            //success message
            response.setResponseCode(1).setResponseMessage("Success");

        } else  {
            //failure message
            response.setResponseCode(0).setResponseMessage("Invalid username or password");
        }

        responseObserver.onNext(response.build());
        responseObserver.onCompleted();
    }

    @Override
    public void logout(User.Empty request, StreamObserver<User.APIResponse> responseObserver) {

    }
    
}
