import React from 'react';


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {noteText: '', project: props.projects[0]?.url, author: props.users[0]?.url}
    }


    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createToDo(this.state.noteText, this.state.project, this.state.author)
        event.preventDefault()
    }

    render() {
        return(
            <form onSubmit={(event)=> this.handleSubmit(event)}>

                <div className="form-group">
                    <label for="noteText">noteText</label>
                    <input type="noteText" className="form-control" name="noteText" value={this.state.noteText} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="project">project</label>
                    <select name="project" className="field field-multiple form-control"
                            onChange={(event) => this.handleChange(event)}
                            value={this.state.options}>
                        {this.props.projects.map((item) => <option value={item.url}>{item.name}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label for="author">author</label>
                    <select name="author" className="field field-multiple form-control"
                            onChange={(event) => this.handleChange(event)}
                            value={this.state.options}>
                        {this.props.users.map((item) => <option value={item.url}>{item.username}</option>)}
                    </select>
                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default ToDoForm;