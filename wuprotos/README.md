<!-- define variables -->
[1.1]: http://i.imgur.com/M4fJ65n.png (ATTENTION)

WUProtos [![Build Status](https://travis-ci.org/Furtif/WUProtos.svg?branch=master)](https://travis-ci.org/Furtif/WUProtos) [![Maintainability](https://api.codeclimate.com/v1/badges/86d147c2b7a696427f0a/maintainability)](https://codeclimate.com/github/Furtif/WUProtos/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/86d147c2b7a696427f0a/test_coverage)](https://codeclimate.com/github/Furtif/WUProtos/test_coverage) [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/rocketbot)
===================

![alt text][1.1] <strong><em>`The contents of this repo are a proof of concept and are for educational use only`</em></strong>![alt text][1.1]<br/>

This repository contains the [ProtoBuf](https://github.com/google/protobuf) `.proto` files needed to decode the Harry Potter: Wizards Unite RPC.

### Implemented messages types
 - [``Global``](https://github.com/Furtif/WUProtos/blob/master/src/WUProtos/Networking/Requests/RequestType.proto)
 - [``Platform``](https://github.com/Furtif/WUProtos/blob/master/src/WUProtos/Networking/Platform/PlatformRequestType.proto) 
   
### Versioning

We are following [semantic versioning](http://semver.org/) for WUProtos.  Every version will be mapped to their current Harry Potter: Wizards Unite version.

| Version      | API           | Notes           | Extra                     |
|--------------|---------------|-----------------|---------------------------|
| 1.0.0.2-beta | 0.8.0-beta    | Initial         |  Protocol Buffers v3.7.1  |

### Usage

If you want to figure out the current version in an automated system, use this file.

[.current-version](https://raw.githubusercontent.com/Furtif/WUProtos/master/.current-version)

*Note: This file will contain pre-release versions too.*

### Preparation

Current recommended protoc version: "Protocol Buffers v3.7.1".

You can find download links [here](https://github.com/google/protobuf/releases).

#### Windows
Be sure to add `protoc` to your environmental path.

#### *nix
Ensure that you have the newest version of `protoc` installed.

#### OS X
Use `homebrew` to install `protobuf ` with `brew install --devel protobuf`.

### Compilation
The compilation creates output specifically for the target language, i.e. respecting naming conventions, etc.  
This is an example of how the generated code will be organized:

```
python compile.py php:
 - WUProtos/* -> WUProtos/*.php
```
```
python compile.py cpp:
 - WUProtos/*-> WUProtos/*.pb.cpp
```
```
python compile.py csharp:
 - WUProtos/* -> WUProtos/*.g.cs
 ```
 ```
 python compile.py objc:
  - WUProtos/* -> WUProtos/*.pbobjc.m
 ```
 ```
 python compile.py python:
  - WUProtos/* -> wuprotos/*_pb2.py
 ```
 ```
 python compile.py ruby:
  - WUProtos/* -> wuprotos/*.rb
 ```
 
![alt text][1.1] //TODO: Need help or test...// ![alt text][1.1] 
  
 ```
python compile.py go:
 - WUProtos/* -> github.com/furtif/wuprotos/*.pb.go
```
```
python compile.py java:
 - WUProtos/* -> com/github/furtif/wuprotos/*.java
 ```
 ```
python compile.py js:
 - WUProtos/*-> wuprotos/*.js
``` 
```
python compile.py rust:
 - WUProtos/* -> WUProtos/*.rs
```
```
python compile.py swift:
 - WUProtos/* -> WUProtos/*.swift
```

### Extra information

 - Run ```python compile.py --help``` for help.
 - You can find all available languages here [https://github.com/google/protobuf](https://github.com/google/protobuf).

### Libraries

If you don't want to compile WUProtos but instead use it directly, check out the following repository.

| Language              | Source                                                         | Status |
|-----------------------|----------------------------------------------------------------|--------|
| Java                  | https://github.com/hpwizardsunite-dev-contrib/WUProtos-Java    |  OK    |