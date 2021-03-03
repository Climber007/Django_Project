import React from 'react';
import { Link, Redirect } from "react-router-dom";
import { postService as service } from '../service/post';
import { observer } from 'mobx-react';
import { message, List } from 'antd';
import { inject } from '../utils';

import 'antd/lib/message/style';
import 'antd/lib/list/style';


@inject({ service }) // {servie:service} => service=service
@observer
export default class L extends React.Component {
    constructor(props) {
        super(props);
        console.log(props);
        props.service.list(props.location.search); //?page=1&id=2
    }

    handleChange(page, pageSize) {
        console.log(page); // 未来的当前页， 当前点击的页码2
        console.log(pageSize);
        console.log('*******************')
        this.props.service.list(`?page=${page}&size=${pageSize}`);
    }

    render() {
        const data = this.props.service.posts;
        if (data.length){
            const {page:current=1, size:pageSize=20, count:total=0} = this.props.service.pagination;
            return (<List
                header={<div>博客列表</div>}
                bordered
                dataSource={data}
                renderItem={item => (<List.Item>
                    <Link to={'/detail/'+item.post_id}>{item.title}</Link>
                    </List.Item>)}
                pagination={{
                    current:current,
                    pageSize:pageSize,
                    total:total,
                    onChange:this.handleChange.bind(this)
                }}
              />);
        } else {
            return <div>无数据</div>
        }
        
    }
}





