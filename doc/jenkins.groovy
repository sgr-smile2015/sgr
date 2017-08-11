#!/usr/bin/groovy

import groovy.json.JsonSlurper 

//get jenkins job_name
def build = Thread.currentThread().toString()
def regexp= ".+?/job/([^/]+)/.*"
def match = build  =~ regexp
def job_name = match[0][1]

//get docker images tags
def  url = 'http://sgr0.docker.com/api/repositories/common/java/tags'
def tags = url.toURL().text
def s = new JsonSlurper()
def object = s.parseText(tags)

return object
