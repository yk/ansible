docker run --name web -p "8080:8080" -v ~/web/root:/site:z -v ~/web/nginx.conf:/etc/nginx/conf.d/example.conf:z -d nginx
