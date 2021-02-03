import React,{Component} from 'react';
import logo from './logo.svg';
import './App.css';
import firebase from './firebase';

class App extends React.Component {
  constructor(props){
    super(props);
  }

    async componentDidMount() {
      const messaging = firebase.messaging();
      await Notification.requestPermission().then(()=>{
          return messaging.getToken();
      }).then((token)=>{
          console.log("token: ",token);
      }).catch(()=>{
            console.log('error');
          })
      messaging.onMessage(function(payload) {
          console.log("onMessage: ", payload);
      });
      navigator.serviceWorker.addEventListener("message", (message) => console.log(message)); 
  }

  
  
  render(){
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
           ASKING FOR PERMISSION, GETTING TOKEN ON ALLOW, 
           THROUGH FIREBASE COMPOSER GETTING NOTIFICATION 
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
