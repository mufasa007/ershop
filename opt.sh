## 添加 GitHub 远程仓库（名称可自定义为 origin）
#git remote add github https://github.com/mufasa007/ershop.git
## 添加 Gitee 远程仓库（名称可自定义为 gitee）
#git remote add gitee https://gitee.com/Mufasa007/ershop.git


  git add .
  git commit -m "$1"
#  git push
#  git push github
#  git push gitee

    # 推送到 GitHub
  git push -u github master
  # 推送到 Gitee
  git push -u gitee master