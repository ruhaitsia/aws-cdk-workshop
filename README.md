# 利用CDK快速实现AWS跨区域文件拷贝

现在，越来越多的中国公司，在AWS海外区域部署业务。利用 S3 作为数据湖，存储海量的数据，包括图片、视频、日志、备份等等。很多场景下，需要把海外的 
S3 数据复制到中国，在中国进行进一步分析处理。AWS  S3 在海外提供跨区域自动复制功能 (Cross region replication, CRR) 。由于中国和
海外区域隔离，不能使用CRR功能。但是通过Lambda和S3的multipart upload接口，我们可以轻松实现跨区域拷贝。请参阅博客文章[分布式 Lambda 从海外到中国自动同步S3文件](http://coolsearch.s3-website-us-east-1.amazonaws.com/ "分布式 Lambda 从海外到中国自动同步S3文件")
了解不同方案的细节。

[分布式 Lambda 从海外到中国自动同步S3文件](http://coolsearch.s3-website-us-east-1.amazonaws.com/ "分布式 Lambda 从海外到中国自动同步S3文件")
提供了详细的解决方案，如果我们想要更进一步，让程序自动帮忙我们创建资源，一键实现方案部署，应该如何去做呢？借助AWS CDK可以轻松帮我们实现一键部署。

我们以[分布式 Lambda 从海外到中国自动同步S3文件](http://coolsearch.s3-website-us-east-1.amazonaws.com/ "分布式 Lambda 从海外到中国自动同步S3文件")文中方案3为例，
指导大家利用AWS CDK实现一键部署。方案3的架构图如下：

![架构图](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/Lambda+(3).png "Demo")


## 环境准备
准备使用AWS CDK之前，我们需要做一些环境准备的工作。
* 安装最新的Node运行时环境
* 通过命令`npm install -g aws-cdk`安装aws cdk
* 配置AWS CLI，将国内和国外region的信息配置好
* 本案例我们使用python作为编程语言，我们配置好python运行时环境。python version > 3.6
* 我们使用PyCharm作为开发IDE

## 克隆代码，并安装相关依赖包
通过Git克隆命令，将该repo的代码下载到本地，通过PyCharm打开代码所在文件夹，进入到PyCharm的终端(Terminal)

手动创建virtualenv(MacOS and Linux):

```
$ python3 -m venv .env
```

virtualenv创建好, 通过以下命令启用该配置(MacOS and Linux)：

```
$ source .env/bin/activate
```

如果你使用的是Windows平台, 可以通过以下命令启用该配置:

```
% .env\Scripts\activate.bat
```

通过以下命令安装应用程序需要的依赖包：

```
$ pip install -r requirements.txt
```

## 修改相关配置
找到credential目录，将国内AWS account中用户的Access Key和Access Secret Key配置到S3BJScredential.txt文件中

找到app.py文件，将你需要创建资源的region和账户信息填入env变量中
* `MyStack(app, "crrcopy-cdk-1", env={'account': '','region': ''})`

找到crrcopy_stack.py文件，将bucket `s3-crr-zhy` 替换成你的s3 bucket


## Bootstrapping环境和部署
第一次部署AWS CDK app到AWS某个区域，需要安装一个`bootstrap stack`，我们可以通过以下命令安装，profile参数跟你AWS CLI的配置保持一致

```
cdk bootstrap --profile tokyo
```

通过以下命令进行环境部署

```
cdk deploy crrcopy-cdk-1 --profile tokyo
```

当成功部署，控制台会打印出成功的信息。


# Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

