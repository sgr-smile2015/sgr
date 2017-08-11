#!/usr/bin/groovy

//所用到的jenkins插件是Extended Choice Parameter Plug-In
//该脚本是获取当前的进程的job名称,使用job名称查找对应的docker
//images tags
import groovy.json.JsonSlurper 

//get jenkins job_name
def build = Thread.currentThread().toString()
def regexp= ".+?/job/([^/]+)/.*"
def match = build  =~ regexp
def job_name = match[0][1]

//get docker images tags
//def  url = 'http://sgr0.docker.com/api/repositories/common/java/tags'
def  url = 'http://sgr0.docker.com/api/repositories/' + job_name + '/java/tags'
def tags = url.toURL().text
def s = new JsonSlurper()
def object = s.parseText(tags)

return object
