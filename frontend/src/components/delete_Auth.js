import React from 'react'

class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {login: '', password: ''}
    }

    handleChange(event) /*event - событие, которое произойдёт, когда пользователь будет вводить данные.*/
    {
        this.setState(
            {
                [event.target.name]: event.target.value /*здесь name - логин или пароль, а value -  введённое значение логина или пароля.*/
            }
        );
    }

    /*Ниже handleSubmit будет выполняться при отправке формы. По нему мы проверяем, что получили логин и пароль, */
    handleSubmit(event) {
        this.props.get_token(this.state.login, this.state.password) /*Вообще через props всегда идёт обращение к верхнему компоненту.*/
    event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
            <input type="text" name="login" placeholder="login" value={this.state.login} onChange={(event)=>this.handleChange(event)} />
            <input type="password" name="password" placeholder="password" value={this.state.password} onChange={(event)=>this.handleChange(event)} />
            <input type="submit" value="Login" />
            </form>
        );
    }
}

export default LoginForm;