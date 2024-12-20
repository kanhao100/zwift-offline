# zoffline_CN

zoffline 通过充当部分 Zwift 服务器的实现,使得可以离线使用 [Zwift](http://zwift.com)。默认情况下 zoffline 仅支持单人游戏。查看[步骤 6: 启用多人游戏](#step-6-可选-启用多人游戏)了解如何启用多用户/多配置文件支持。

zoffline 还提供了与幽灵(你之前的骑行记录)一起骑行的功能。通过在 zoffline 启动器中勾选"Enable ghosts"来启用此功能。查看[额外功能](#额外功能)了解更多详情。

此外,zoffline 的启动器允许选择特定地图进行骑行,无需修改配置文件。

## 安装

设置 zoffline 需要两个主要步骤。首先,在运行 Zwift 之前必须在系统上安装并运行 zoffline(可以是运行 Zwift 的系统或本地网络中的另一个系统)。其次,必须将 Zwift 配置为使用 zoffline 而不是官方 Zwift 服务器。

### 步骤 1: 安装 zoffline
根据你的平台,有三种安装和运行 zoffline 的方式:

<details><summary>最简单方式(仅限 Windows)</summary>
在 Windows 上安装 zoffline:

* 从 https://github.com/zoffline/zwift-offline/releases/latest 下载最新的 zoffline 发布版
* 如果你不是在运行 Zwift 的同一台电脑上运行 zoffline:在 ``storage`` 目录中创建一个 ``server-ip.txt`` 文件,其中包含运行 zoffline 的电脑的 IP 地址。
* 运行下载的 zoffline.exe
  * 运行后,zoffline 将在同一文件夹中创建一个 ``storage`` 目录来存储你的 Zwift 进度。
* 在 zoffline.exe 运行的情况下启动 Zwift (__完成步骤 2 后__ 或运行 https://github.com/oldnapalm/zoffline-helper/releases/latest 中的 __configure_client__ 脚本)
  * zoffline 需要几秒钟才能启动。等待命令提示符中出现文本后再打开 Zwift。
* 使用完 Zwift 后,在命令行中按 Ctrl+C 关闭 zoffline。
</details>

<details><summary>Linux、Windows 或 macOS(从源代码)</summary>
在 Linux、Windows 或 macOS 上安装 zoffline:

* 如果尚未安装,请安装 Python 3 (https://www.python.org/downloads/)
  * 在 Windows 上,强烈建议通过 Microsoft Store 安装 Python! 如果使用 Python 安装程序,请确保在第一个 Python 安装程序界面中勾选"Add Python 3.x to PATH"。
* 克隆或下载此仓库
* 安装依赖
  * 例如,在 Linux/Mac 上: ``pip3 install -r requirements.txt``
  * 例如,在 Windows 命令提示符中: ``pip install -r requirements.txt``
    * 你可能需要使用 ``C:\Users\<username>\AppData\Local\Programs\Python\Python<version>\Scripts\pip.exe`` 而不是仅使用 ``pip``
* 如果你不是在运行 Zwift 的同一台电脑上运行 zoffline:在 ``storage`` 目录中创建一个 ``server-ip.txt`` 文件,其中包含运行 zoffline 的电脑的 IP 地址。
* 在启动 Zwift 之前运行 standalone.py
  * 例如,在 Linux/Mac 上: ``sudo ./standalone.py``
    * 需要 sudo 因为我们要绑定特权端口 80 和 443。
    * 如果 Python 3 不是你的系统默认版本,运行 ``sudo python3 standalone.py``
  * 例如,在 Windows 命令提示符中: ``python standalone.py``
    * 你可能需要使用 ``C:\Users\<username>\AppData\Local\Programs\Python\Python<version>\python.exe`` 而不是仅使用 ``python``
* 在 standalone.py 运行的情况下启动 Zwift (__完成步骤 2 后__)
* 注意:升级 zoffline 时,请确保保留 ``storage`` 目录。它包含你的 Zwift 进度状态。

zoffline 可以安装在与 Zwift 相同的机器上或另一台本地机器上。
</details>

<details><summary>使用 Docker</summary>
 
* 安装 Docker
* 使用以下命令创建 docker 容器:<br>
  ``docker create --name zwift-offline -p 443:443 -p 80:80 -p 3024:3024/udp -p 3025:3025 -p 53:53/udp -v </path/to/host/storage>:/usr/src/app/zwift-offline/storage -e TZ=<timezone> zoffline/zoffline``
  * 如果你不在意 zoffline 更新时是否保留 Zwift 进度状态(不太可能),可以选择不包含 ``-v </path/to/host/storage>:/usr/src/app/zwift-offline/storage``
  * 传递给 ``-v`` 的路径可能需要全局可读写。
  * 有效的 ``<timezone>`` 值列表(例如 America/New_York)可以在[这里](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)找到。
  * 如果你使用 Docker v1.9.0 或更高版本,添加 ``--restart unless-stopped`` 将使 zoffline 在启动时自动启动。
* 如果你不是在运行 Zwift 的同一台电脑上运行 zoffline:在 ``</path/to/host/storage>`` 目录中创建一个 ``server-ip.txt`` 文件,其中包含运行 zoffline 的电脑的 IP 地址。
* 使用以下命令启动 zoffline:
  ``docker start zwift-offline``
</details>

<details><summary>使用 Docker Compose</summary>
 
* 安装 docker-compose
* 可以使用此仓库中的 ``docker-compose.yml`` 文件(将从 Dockerfile 构建),或使用此示例 compose 文件:
   ```
  version: "3.3"
  services:
      zoffline:
           image: zoffline/zoffline:latest
           container_name: zoffline
           environment:
              - TZ=Europe/London
           volumes:
              - ./storage/:/usr/src/app/zwift-offline/storage
           ports:
              - 80:80
              - 443:443
              - 3024:3024/udp
              - 3025:3025
           restart: unless-stopped    
   ```
  * 在 ``volumes`` 标签中,将 ``:`` 前的 ``./storage/`` 替换为你想用作本地 zoffline 数据存储的目录路径。
* 如果你不是在运行 Zwift 的同一台电脑上运行 zoffline:在 ``storage`` 目录中创建一个 ``server-ip.txt`` 文件,其中包含运行 zoffline 的电脑的 IP 地址。
* 使用以下命令启动 zoffline:
  ``docker-compose up -d ``
</details>

### 步骤 2: 配置 Zwift 客户端使用 zoffline

<details><summary>Windows 说明</summary>

* 如果尚未安装,请安装 Zwift
* __注意:__ 你可以不执行以下步骤,而是运行 https://github.com/oldnapalm/zoffline-helper/releases/latest 中的 __configure_client__ 脚本
* 在运行 Zwift 的 Windows 机器上,将此仓库中的以下文件复制到已知位置:
  * [ssl/cert-zwift-com.p12](https://github.com/zoffline/zwift-offline/raw/master/ssl/cert-zwift-com.p12)
  * [ssl/cert-zwift-com.pem](https://github.com/zoffline/zwift-offline/raw/master/ssl/cert-zwift-com.pem)
* 以管理员身份打开命令提示符,cd 到该位置并运行
  * ``certutil.exe -importpfx Root cert-zwift-com.p12``
  * 如果提示输入密码,直接留空即可。没有密码。
* 以管理员身份打开记事本并打开 ``C:\Program Files (x86)\Zwift\data\cacert.pem``
  * 将 ``ssl/cert-zwift-com.pem`` 的内容追��到 cacert.pem
* 以管理员身份打开记事本并打开 ``C:\Windows\System32\Drivers\etc\hosts``
  * 追加此行: ``<zoffline ip> us-or-rly101.zwift.com secure.zwift.com cdn.zwift.com launcher.zwift.com``
    <br />(其中 ``<zoffline ip>`` 是运行 zoffline 的机器的 IP 地址。如果
    它与 Zwift 运行在同一台机器上,使用 ``127.0.0.1`` 作为 IP。)
* 如果你希望在 ``hosts`` 文件中仅在特别使用 zoffline 时进行更改,你可以选择使用 ``scripts`` 目录中的 __launch.bat__ 脚本来启动 zoffline,而不是使用普通的 Zwift Launcher。详见 [#121](https://github.com/zoffline/zwift-offline/issues/121)。

原因:我们需要将 Zwift 重定向到使用 zoffline,并说服 Windows 和 Zwift 接受
zoffline 为 Zwift 域名签发的自签名证书。你也可以生成自己的证书并执行相同操作。

</details>

<details><summary>macOS 说明</summary>

* 如果尚未安装,请安装 Zwift
* 在运行 Zwift 的 Mac 机器上,将此仓库中的文件 [ssl/cert-zwift-com.pem](https://github.com/zoffline/zwift-offline/raw/master/ssl/cert-zwift-com.pem) 复制到已知位置。
* 打开钥匙串访问,在"钥匙串"下选择"系统",在"类别"下选择"证书"
    * 点击"文件 - 导入项目..."并导入 cert-zwift-com.pem
    * 右键点击 "\*.zwift.com",选择"��示简介"并在"信任"下选择"使用此证书时:始终信任"。
* 从 cert-zwift-com.pem 所在位置,运行 ``sed -n '29,53p' cert-zwift-com.pem >> ~/Library/Application\ Support/Zwift/data/cacert.pem``
* 使用文本编辑器(需要管理员权限)打开 ``/etc/hosts``
  * 追加此行: ``<zoffline ip> us-or-rly101.zwift.com secure.zwift.com cdn.zwift.com launcher.zwift.com``
    <br />(其中 ``<zoffline ip>`` 是运行 zoffline 的机器的 IP 地址。如果
    它与 Zwift 运行在同一台机器上,使用 ``127.0.0.1`` 作为 IP。)

原因:我们需要将 Zwift 重定向到使用 zoffline,并说服 macOS 和 Zwift 接受
zoffline 为 Zwift 域名签发的自签名证书。你也可以生成自己的证书并执行相同操作。

</details>

<details><summary>Android (非 root 设备)</summary>

* 安装所需应用:
  * 从[这里](https://github.com/Argon2000/ZofflineObbAndroid/releases/latest)下载并安装 ``ZofflineObb.apk``
  * 从[这里](https://github.com/x-falcon/Virtual-Hosts/releases/latest)下载并安装 ``app-Github-release.apk``
  * 创建一个 `hosts.txt` 文件以供应用使用(你可以使用文本编辑器应用或使用在线工具如[这个](https://passwordsgenerator.net/text-editor/)在线创建)。文件必须如下所示(将 ``<zoffline ip>`` 替换为运行 zoffline 的机器的 IP 地��):
  ```
  <zoffline ip> us-or-rly101.zwift.com
  <zoffline ip> secure.zwift.com
  <zoffline ip> cdn.zwift.com
  ```
  * 在 Android 设置中关闭"私人 DNS"
  * 运行"Virtual Hosts"并选择创建的 `hosts.txt` 文件
  * 或者,不使用"Virtual Hosts"应用,你可以在 ``storage`` 目录中创建一个 ``fake-dns.txt`` 文件,并将手机 Wi-Fi 连接的"DNS 1"设置为运行 zoffline 的电脑的 IP 地址
  * 注意:如果你知道自己在做什么并且有足够功能的路由器,你可以调整路由器来更改这些 DNS 记录,而不是使用"Virtual Hosts"应用或更改手机 DNS。
* 每次安装或更新后修补:
  * 从 Google play 安装/更新 Zwift,但不要立即启动。
    * 如果你已经启动过它,请转到 `Android 设置 > 应用 > Zwift` 并清除数据或卸载并重新安装应用。
  * 打开 `ZofflineObb` 应用并运行它(允许访问存储)
  * 等待进程完成(5-10分钟)
  * 运行 Zwift,希望它能验证下载并运行
* 玩 Zwift:
  * Virtual Hosts 按钮必须处于 ON 状态
  * 启动 Zwift 并使用任何电子邮件/密码登录,如果启用了多人游戏则创建新用户。

原因:我们需要将 Zwift 重定向到使用 zoffline(这由 Virtual Hosts 应用完成)并说服 Zwift 接受
zoffline 为 Zwift 域名签发的自签名证书(这由修补工具 ZofflineObb 完成)。

</details>

<details><summary>Android (已 root 设备)</summary>

* 在设备上安装 Zwift
* 打开 Zwift 一次以完成安装(即下载所有额外文件)。
* 将 ``ssl/cert-zwift-com.pem`` 的内容追加到设备上的 ``/data/data/com.zwift.zwiftgame/dataES/cacert.pem``
  * 注意:此文件仅在首次运行 Zwift 后才会存在,因为它是在初始安装后下载的
  * 如果你的设备没有文本编辑器,这是一个简单的方法:
    * ``adb push ssl/cert-zwift-com.pem /data/data/com.zwift.zwiftgame/dataES/``
    * 在 ``adb shell`` 中: ``cd /data/data/com.zwift.zwiftgame/dataES/``
    * 在 ``adb shell`` 中: ``cat cert-zwift-com.pem >> cacert.pem``
    * 无论你如何操作,都要确保文件的权限和所有权保持不变。
* 修改设备的 ``/etc/hosts`` 文件
  * 追加此行: ``<zoffline ip> us-or-rly101.zwift.com secure.zwift.com cdn.zwift.com``
    <br />(其中 ``<zoffline ip>`` 是运行 zoffline 的机器的 IP 地址。)
  * 如果设备上没有文本编辑器,建议:
    * ``adb pull /etc/hosts``
    * (在 PC 上修改)
    * ``adb push hosts /etc/hosts``
  * 注意:如果你知道自己在做什么并且有足够功能的路由器,你可以调整路由器来更改这些 DNS 记录,而不是修改你的 ``hosts`` 文件。
* 启动 Zwift 并使用任何电子邮件/密码登录,如果启用了多人游戏则创建新用户。

原因:我们需要将 Zwift 重定向到使用 zoffline 并说服 Zwift 接受
zoffline 为 Zwift 域名签发的自签名证书。你也可以生成自己的证书并执行相同操作。

</details>

#### 启用/禁用 zoffline

要像正常一样在线使用 Zwift,在启动 Zwift 之前注释掉或删除添加到 ``hosts``
文件中的行。然后确保完全关闭 Zwift(右键点击 Zwift 系统托盘图标并退出)并重启 Zwift。


### 步骤 3 [可选]: 获取当前 Zwift 配置文件

<details><summary>展开</summary>

如果你在首次启用 zoffline 启动 Zwift 之前没有获取当前的 Zwift 配置文件,
系统会提示你创建一个新的配置文件(身高、体重、性别)。你的配置文件可以通过游戏内
菜单进一步自定义和更改(例如姓名、国籍、体重变化等)。

要获取你当前的配置文件:
* __注意:__ 你可以不执行以下步骤,而是使用启动器窗口中的"Settings - Zwift"按钮(如果使用 Android,访问 ``https://<zoffline_ip>/profile/zoffline/``)。
* 确保禁用 zoffline。
* 运行 ``scripts/get_profile.py -u <your_zwift_username>``
  * 或者,如果使用 Windows zoffline.exe 版本且未安装 Python,你可以运行从 https://github.com/oldnapalm/zoffline-helper/releases/latest 获取的 ``get_profile.exe`` 来代替 ``scripts/get_profile.py``
* 将生成的 ``profile.bin``、``achievements.bin`` 和 ``economy_config.txt`` (保存在运行 get_profile.py 的目录中)移动到 ``storage/1`` 目录。
  * 如果在 Windows 上使用 zoffline.exe,如果 ``storage/1`` 目录不存在,请在与 zoffline.exe 相同的文件夹中创建它。
  * 如果使用 Docker,目录 ``1`` 应该在你传递给 ``-v`` 的路径中。

</details>

### 步骤 4 [可选]: 上传活动

<details><summary>Strava</summary>

* 从 https://www.strava.com/settings/api 获取 CLIENT_ID 和 CLIENT_SECRET
* __注意:__ 你可以不执行以下步骤,而是将 API 应用程序的授权回调域设置为 ``launcher.zwift.com`` 并使用启动器窗口中的"Settings - Strava"按钮(仅限 Windows 和 macOS)。
* 运行 ``scripts/strava_auth.py --client-id CLIENT_ID --client-secret CLIENT_SECRET``
  * 或者,如果使用 Windows zoffline.exe 版本且未安装 Python,你可以运行从 https://github.com/oldnapalm/zoffline-helper/releases/latest 获取的 ``strava_auth.exe`` 来代替 ``scripts/strava_auth.py``
* 打开 http://localhost:8000/ 并授权。
* 将生成的 ``strava_token.txt`` (保存在运行 ``strava_auth.py`` 的目录中)移动到 ``storage/1`` 目录。
* 如果测试,至少骑行 300 米,更短的活动不会上传。
* 无法自动上传��图,详见 [#28](https://github.com/zoffline/zwift-offline/issues/28)。

</details>

<details><summary>Garmin Connect</summary>

* 如果从源代码运行,安装 garth: ``pip install garth``
* 如果需要,在 ``storage`` 目录中创建一个 ``garmin_domain.txt`` 文件,其中包含域名
  * 对于中国使用 ``garmin.cn``
* 使用启动器窗口中的"Settings - Garmin"按钮输入你的凭据(如果使用 Android,访问 ``https://<zoffline_ip>/garmin/zoffline/``)。
* 如果你的账户启用了多因素认证,运行脚本 ``garmin_auth.py`` 并将生成的 ``garth`` 文件夹(保存在运行 ``garmin_auth.py`` 的目录中)移动到 ``storage/1`` 目录。
  * 或者,如果使用 Windows zoffline.exe 版本且未安装 Python,你可以运行从 https://github.com/oldnapalm/zoffline-helper/releases/latest 获取的 ``garmin_auth.exe`` 来代替。
* 如果测试,至少骑行 300 米,更短的活动不会上传。

</details>

<details><summary>Intervals.icu</summary>

* 使用启动器窗口中的"Settings - Intervals"按钮输入你的凭据(如果使用 Android,访问 ``https://<zoffline_ip>/intervals/zoffline/``)。
* 从 https://intervals.icu/settings 的"Developer Settings"下复制"Athlete ID"和"API Key"。
* 如果测试,至少骑行 300 米,更短的活动不会上传。

</details>

### 步骤 5 [可选]: 安装 Zwift Companion App

<details><summary>Android (非 root 设备)</summary>

* 安装 apk-mitm (https://github.com/shroudedcode/apk-mitm)
* 打开 ``apk-mitm/dist/tools/apktool.js`` (运行 ``npm root -g`` 找到其位置)并按如下方式编辑:
  ``` js
      decode(inputPath, outputPath) {
          return this.run([
              'decode',
              '-resm', // 添加这行
              'dummy', // 添加这行
              inputPath,
              '--output',
              outputPath,
              '--frame-path',
              this.options.frameworkPath,
          ], 'decoding');
      }
  ```
* 将此仓库中的文件 [ssl/cert-zwift-com.pem](https://github.com/zoffline/zwift-offline/raw/master/ssl/cert-zwift-com.pem) 和 Zwift Companion apk (例如 ``zca.apk``)复制到已知位置
* 打开命令提示符,cd 到该位置并运行
  * ``apk-mitm --certificate cert-zwift-com.pem zca.apk``
* 将 ``zca-patched.apk`` 复制到你的手机并安装
* 从[这里](https://github.com/x-falcon/Virtual-Hosts/releases/latest)下载并安装 ``app-Github-release.apk``
* 创建一个 ``hosts.txt`` 文件以供应用使用(你可以使用文本编辑器应用或使用在线工具如[这个](https://passwordsgenerator.net/text-editor/)在线创建)。文件必须如下所示(将 ``<zoffline ip>`` 替换为运行 zoffline 的机器的 IP 地址):
  ```
  <zoffline ip> us-or-rly101.zwift.com
  <zoffline ip> secure.zwift.com
  ```
  * 重要:不要将 ``cdn.zwift.com`` 添加到 ``hosts.txt``,Companion 需要从官方服务器下载图片
* 在 Android 设置中关闭"私人 DNS"
* 运行"Virtual Hosts"并选择创建的 ``hosts.txt`` 文件
* 或者,不使用"Virtual Hosts"应用,你可以在 ``storage`` 目录中创建一个 ``fake-dns.txt`` 文件,并将手机 Wi-Fi 连接的"DNS 1"设置为运行 zoffline 的电脑的 IP 地址
* 注意:如果你知道自己在做什么并且有足够功能的路由器,你可以调整路由器来更改这些 DNS 记录,而不是使用"Virtual Hosts"应用或更改手机 DNS。

</details>

### 步骤 6 [可选]: 启用多人游戏

<details><summary>展开</summary>

要启用多用户支持,请执行以下步骤:

* 在 ``storage`` 目录中创建一个 ``multiplayer.txt`` 文件。
* 如果你不是在运行 Zwift 的同一台电脑上运行 zoffline:在 ``storage`` 目录中创建一个 ``server-ip.txt`` 文件,其中包含运行 zoffline 的电脑的 IP 地址。
  * 如果 zoffline 远程运行,则需要在运行 zoffline 的电脑上打开 TCP 端口 80、443、3025 和 UDP 端口 3024。
* 启动 Zwift 并创建一个账户。
  * 此账户仅存在于你的 zoffline 服务器上,与你的实际 Zwift 账户无关。
* 要启用密码重置功能:在 ``storage`` 目录中创建一个 ``gmail_credentials.txt`` 文件,其中包含 Gmail 账户的登录凭据。你需要访问 https://security.google.com/settings/security/apppasswords 并创建一个应用密码以允许从服务器登录。

</details>

### 额外功能

<details><summary>幽灵</summary>

* 通过在 zoffline 的启动器中勾选"Enable ghosts"启用此功能(如果使用 Android,访问 ``https://<zoffline_ip>/user/zoffline/``,勾选"Enable ghosts"并点击"Start Zwift"保存选项)。
* 当你保存活动时,幽灵将保存在 ``storage/<player_id>/ghosts/<world>/<route>`` 中。下次你骑行相同路线时,幽灵将被加载。
* 在聊天中输入 ``.regroup`` 可以重组幽灵。
* 可以通过在 ``storage`` 文件夹中创建 ``ghost_profile.txt`` 文件来自定义装备。脚本 ``find_equip.py`` 可用于填充此文件。
</details>

<details><summary>机器人</summary>

* 在 ``storage`` 文件夹中创建 ``enable_bots.txt`` 文件以将幽灵加载为机器人,它们将继续骑行,无论你骑行的路线如何。
* 可选地,``enable_bots.txt`` 可以包含一个乘数值(请注意,如果产生的机器人数量太多,可能会导致性能问题或完全无法工作)。
* 可以通过在 ``storage`` 文件夹中创建 ``bot.txt`` 文件来自定义名字、国籍和装备。脚本 ``get_pro_names.py`` 可用于填充此文件。
* 如果你想要一些随机机器人,请查看[这个仓库](https://github.com/oldnapalm/zoffline-bots)。
</details>

<details><summary>机器陪骑员</summary>

* 机器陪骑员是使用功率模拟器保存的幽灵,你可以在[这个仓库](https://github.com/oldnapalm/zoffline-bots)中找到一些。
* 幽灵必须使用 1 秒的更新频率记录(默认为 3 秒)。
* 活动必须在相同的位置和速度开始和结束,否则机器人不会平滑循环。
* 配置文件必须包含唯一的玩家 ID 和路线 ID,这样当你加入机器人时,在交叉路口会走相同的转弯。
* 脚本 ``bot_editor.py`` 可用于修改 ``profile.bin`` (设置名字、玩家 ID 和路线 ID)和 ``route.bin`` (剪切多余的点以形成完美循环)。
* 如果你想创建一个动态机器陪骑员(在上坡时增加功率,下坡时减少功率),你可以使用 [standalone_power.py](https://github.com/oldnapalm/zwift-offline/blob/master/standalone_power.py) (需要 2 个 ANT 接收器,[python-ant](https://github.com/mch/python-ant) 和 [PowerMeterTx.py](https://github.com/oldnapalm/zwift-offline/blob/master/PowerMeterTx.py))。
</details>

<details><summary>书签</summary>

* 当你完成一个活动时,你的最后位置将被保存为书签。
* 也可以使用聊天中的 ``.bookmark <name>`` 命令保存书签。
* 你可以通过在主屏幕上的"Join a Zwifter"中选择书签来从书签开始新的活动。
* 你可以使用动作栏上的传送图标传送到书签位置。
</details>

<details><summary>全时段排行榜</summary>

* 要启用全时段排行榜(覆盖 60 分钟实时结果和 90 天个人记录),在 ``storage`` 目录中创建一个 ``all_time_leaderboards.txt`` 文件。
* 领骑衫仍然只在 60 分钟内有效,但只有在创造新的全时段记录时才会授予。
</details>

<details><summary>解锁特权</summary>

* 要解锁特权(特殊装备),在 ``storage`` 目录中创建一个 ``unlock_entitlements.txt`` 文件。
* 要解锁所有装备,请创建一个 ``unlock_all_equipment.txt`` 文件。
</details>

<details><summary>CDN 代理</summary>

* 要从 Zwift 服务器获取官方地图时间表和更新文件:在 ``storage`` 目录中创建一个 ``cdn-proxy.txt`` 文件。这只有在你在与 Zwift 客户端不同的机器上运行 zoffline 时才能工作。
* 默认情况下,zoffline 将尝试使用 Google 公共 DNS 来解析 Zwift 主机名,即使 zoffline 在与 Zwift 客户端相同的机器上运行也应该可以工作。要避免这种情况,在 ``storage`` 目录中创建一个 ``disable_proxy.txt`` 文件。
* 如果你想从 zoffline 提供更新文件,运行脚本 ``get_gameassets.py`` 来下载游戏文件。
</details>

<details><summary>Discord 桥接</summary>

* Discord 桥接仅在从源代码运行 zoffline 时可用。
* 安装 discord.py: ``pip3 install discord.py``
* 在 ``storage`` 目录中创建一个 ``discord.cfg`` 文件,内容如下
  ```
  [discord]
  token = 
  webhook = 
  channel = 
  welcome_message = 
  help_message = 
  ```
</details>

## 社区 Discord 服务器和 Strava 俱乐部

请加入社区支持的 [Discord](https://discord.gg/GMdn8F8) 服务器和 [Strava](https://www.strava.com/clubs/zoffline) 俱乐部。

## 依赖项

Docker

-或者-

* Python 3 (https://www.python.org/downloads/)
* Flask (https://flask.palletsprojects.com/)
* python-protobuf (https://pypi.org/project/protobuf/)
* pyJWT (https://pyjwt.readthedocs.io/)
* Flask-Login (https://flask-login.readthedocs.io/)
* Flask-SQLAlchemy (https://flask-sqlalchemy.palletsprojects.com/)
* gevent (http://www.gevent.org/)
* pycryptodome (https://pypi.org/project/pycryptodome/)
* dnspython (https://www.dnspython.org/)
* fitdecode (https://pypi.org/project/fitdecode/)
* stravalib (https://stravalib.readthedocs.io/)
* 可选: garth (https://pypi.org/project/garth/)
* 可选: discord.py (https://discordpy.readthedocs.io/)


## 注意

未来的 Zwift 更新可能会导致 zoffline 无法使用,直到它被更新。当启用 zoffline 时,
Zwift 更新将不会安装。如果 zoffline 更新破坏了某些功能,请查看 ``CHANGELOG`` 了解可能需要进行的更改。

不要将 zoffline 暴露在互联网上,它的设计初衷并非如此。

<details><summary>如果 zoffline 落后于 Zwift 的官方客户端</summary>
如果 zoffline 落后于支持最新的 Zwift 客户端,可以更新它以运行最新版本的 Zwift。

* Windows: 将 ``C:\Program Files (x86)\Zwift\Zwift_ver_cur.xml`` 复制到 zoffline 的 ``cdn/gameassets/Zwift_Updates_Root/`` 覆盖现有文件。
* macOS: 将 ``~/Library/Application Support/Zwift/ZwiftMac_ver_cur.xml`` 复制到 zoffline 的 ``cdn/gameassets/Zwift_Updates_Root/`` 覆盖现有文件。
* Linux: 在 zwift-offline 仓库中运行[这个脚本](https://gist.github.com/zoffline/b874e93e24439f0f4fbd7b55f3876fd2)。

注意:不能保证未经测试的 Zwift 更新能与 zoffline 一起工作。然而,从历史上看,Zwift 更新很少会破坏 zoffline。

或者,可以使用[这个脚本](https://gist.github.com/oldnapalm/556c58448a6ee09438b39e1c1c9ce3d0)将 Zwift 降级到 zoffline 支持的版本。
</details>


## 免责声明

Zwift 是 Zwift, Inc. 的商标,该公司与本项目的制作者没有关联,也不认可本项目。

所有产品和公司名称都是其各自持有者的商标。使用它们并不意味着与它们有任何关联或得到它们的认可。

