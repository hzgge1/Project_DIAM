import React, { useState, useEffect } from 'react';
import axios from 'axios';

function LoginPage() {
  const [htmlContent, setHtmlContent] = useState('');

  useEffect(() => {
    axios.get('forum/templates/login_form.html')
      .then(response => {
        setHtmlContent(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div dangerouslySetInnerHTML={{ __html: htmlContent }}></div>
  );
}

export default LoginPage;
