#!/bin/bash

start_add_remote() {
  # 添加 GitHub 远程仓库（名称可自定义为 origin）
  git remote add github https://github.com/mufasa007/ershop.git
  # 添加 Gitee 远程仓库（名称可自定义为 gitee）
  git remote add gitee https://gitee.com/Mufasa007/ershop.git
  # 退出
  exit 1
}

# 修复后的推送方法
start_push() {
  local commit_msg="${1:-Auto commit}"  # 设置默认提交信息

  # 参数校验（兼容空值场景）
  if [[ -z "$commit_msg" ]]; then
    echo "错误：提交信息不能为空！用法: $0 push \"提交信息\""
    exit 1
  fi

  git add .
  git commit -m "$commit_msg" || {
    echo "提交失败！错误码: $?" >&2
    exit 1
  }

  # 推送至双仓库
  git push -u github master && git push -u gitee master || {
    echo "推送失败！请检查网络或权限。错误码: $?" >&2
    exit 1
  }

  echo "推送成功！"

  echo "部署到mufasa007.github.io"
  hexo c && hexo g && hexo d
}

start_generate(){
  echo "开始执行 [npm install -g hexo] "
  npm install -g hexo
  echo "开始执行 [hexo clean] "
  hexo clean
  echo "开始执行 [hexo generate] "
  hexo generate
  echo "开始复制 [ads.txt] "
  cp ./document/ads.txt ./public/ads.txt
  echo "完成执行 [start_generate] "
}

start_clean(){
  echo "开始执行 [hexo clean] "
  hexo clean
  echo "完成执行 [hexo clean] "
}


# 主程序，根据传入的参数调用相应的方法
case "$1" in
    remote)
        start_add_remote
        ;;
    push)
        start_push "$2"
        ;;
    generate)
        start_generate
        ;;
    clean)
        start_clean
        ;;
    *)
        echo "用法: $0 {remote|push}"
        exit 1
        ;;
esac