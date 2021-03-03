import axios from 'axios';
import { observable } from 'mobx';
import store from 'store';

store.addPlugin(require('store/plugins/expire'));

class UserService{
    @observable loggedin = false;
    @observable errMsg = ''; // 错误信息

    login(email, password) {
        // TODO 从view层发来的邮箱和密码，转发给后台服务器
        console.log('~~~~~~~~~~~~~~~~~~')
        console.log(email)
        console.log(password)
        console.log('~~~~~~~~~~~~~~~~~~')

        axios.post('/api/user/login', {
            email:email,
            password:password
          })
          .then(response => {
            console.log(1, response);
            console.log(response.data);
            const {token, user} = response.data;
            console.log(token)
            console.log(user);
            store.set('token', token, new Date().getTime() + 8*3600*1000);
            this.loggedin = true;
          })
          .catch(error => {
            console.log(2, error);
            this.loggedin = false;
            this.errMsg = '用户名密码错误';
          });
       
    }


    reg(email, name, password) {
      // TODO 从view层发来的邮箱和密码，转发给后台服务器
      console.log('~~~~~~~~~~~~~~~~~~')
      console.log(name)
      console.log(email)
      console.log(password)
      console.log('~~~~~~~~~~~~~~~~~~')

      axios.post('/api/user/reg', {
          name, email, password
        })
        .then(response => {
          console.log(1, response);
          console.log(response.data);
          const {token, user} = response.data;
          console.log(token)
          console.log(user);
          store.set('token', token, new Date().getTime() + 8*3600*1000);
          this.loggedin = true;
        })
        .catch(error => {
          console.log(2, error);
          this.loggedin = false;
          this.errMsg = '注册失败';
        });
     
  }
}

const userService = new UserService();

export {userService};



