FROM httpd:2.4

# Copy static frontend files into Apache document root
COPY ./ /usr/local/apache2/htdocs/

# Expose default HTTP port
EXPOSE 80

# Use default httpd CMD