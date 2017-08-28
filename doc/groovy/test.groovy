#!/usr/bin/groovy

import groovy.io.FileType

def list = []

def dir = new File("./work")

dir.eachDir { dirs ->
def text = dirs as String 
//println text.minus("./work/")
def obj = text.minus("./work/")
//println file.isDirectory() ? "DIR: ${file}" : "FILE: ${file}"
def flag = obj =~ '.*@.*'
if (!flag) {
	println 'hello ' + obj
	list << obj
	}

}

println list
println list.size()
