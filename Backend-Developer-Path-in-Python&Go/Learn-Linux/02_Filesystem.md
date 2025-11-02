``` sh
curl -L https://github.com/bootdotdev/worldbanc/archive/refs/heads/main.zip -o worldbanc.zip
unzip worldbanc.zip
rm worldbanc.zip
mv worldbanc-main worldbanc
sudo chown -R $(whoami) worldbanc
sudo chmod -R 755 worldbanc
```

``` sh
# to find word "hello" in file
grep "hello" filename.txt
```


``` sh
# to find files named "*.log" in some directory
find logs/ -name "*.log"
```