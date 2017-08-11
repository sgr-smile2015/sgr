#!/usr/bin/groovy

import groovy.io.FileType

def list = []

def dir = new File(".")

dir.eachDir { dirs ->
def text = dirs as String 
println text.minus("./")
//println file.isDirectory() ? "DIR: ${file}" : "FILE: ${file}"
list << text.minus("./")
}

println list
println list.size()
