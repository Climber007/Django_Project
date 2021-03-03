import axios from 'axios';

import { observable } from 'mobx';
import store from 'store';

store.addPlugin(require('store/plugins/expire'))

class PostService {
  constructor(props) {
    this.axios = axios.create({
      baseURL: '/api/post/'
    });
  }

  @observable msg = '';
  @observable posts = [];
  @observable pagination = { page: 1, size: 20, pages: 1, count: 0 };

  @observable post = {};

  getToken() {
    // 验证，token，在store中是否拿回来过期了，如果过期，清除
    //if (store.getExpiration('token')) return '';
    return store.get('token', '');
  }

  pub(title, content) {
    console.log('~~~~~~~~~~~~~~~~~~')
    console.log(title)
    console.log(content)
    console.log('~~~~~~~~~~~~~~~~~~')

    this.axios.post('pub', {
      title, content
    }, {
        headers: { 'Jwt': this.getToken() }
      })
      .then(response => {
        console.log(1, response);
        console.log(response.data);
        this.msg = '博客提交成功';
      })
      .catch(error => {
        console.log(2, error);
        this.msg = '博客提交失败';
      });
  }

  list(search) {
    console.log('~~~~~~~~~~~~~~~~~~')
    console.log(search)
    console.log('~~~~~~~~~~~~~~~~~~')
    // /list?page=1&size=2 => constructor ?page=1&size=2 => 
    // service list(?page=1&size=2) => /api/post/?page=1&size=2
    this.axios.get(search)
      .then(response => {
        console.log(1, response);
        console.log(response.data); // posts, pagination
        const { posts = [], pagination = {} } = response.data;
        this.posts = posts;
        this.pagination = pagination;
      })
      .catch(error => {
        console.log(2, error);
        this.msg = '博客列表获取失败';
      });
  }

  getPost(id) {
    console.log('~~~~~~~~~~~~~~~~~~')
    console.log(id)
    console.log('~~~~~~~~~~~~~~~~~~')
    // /detail/2 => constructor 2 => 
    // service list(2) => /api/post/2
    this.axios.get(id)
      .then(response => {
        console.log(1, response);
        console.log(response.data); // posts, pagination
        this.post = response.data.post;
      })
      .catch(error => {
        console.log(2, error);
        this.msg = '博客内容获取失败';
      });
  }
}


const postService = new PostService();

export { postService };


