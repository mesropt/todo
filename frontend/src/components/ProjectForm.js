import React from "react";

class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {projectName: '', repositoryLink: '', users: ['']}
    }
    handleChange(event) {
        if (event.target.projectName === 'users') {
            let value = Array.from(
                event.target.selectedOptions,
                (option) => option.value
            );
            this.setState(
                {
                    users: value,
                }
            );
        } else {
            this.setState(
                {
                    [event.target.projectName]: event.target.value
                }
            );
        }
    }

    handleSubmit(event) {
        this.props.createProject(this.state.projectName, this.state.repositoryLink, this.state.users)
        event.preventDefault()
    }

    render() {
        return(
            <form onSubmit={(event)=> this.handleSubmit(event)}>

                <div className="form-group">
                    <label for="projectName">projectName</label>
                    <input type="text" className="form-control" name="name" value={this.state.projectName} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="repositoryLink">repositoryLink</label>
                    <input type="url" required={false} className="form-control" name="repositoryLink" value={this.state.repositoryLink} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="users">users</label>
                    <select multiple={true} name="users" className="field field-multiple form-control"
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

export default ProjectForm;