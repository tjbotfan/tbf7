using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

using System.Net;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using uPLibrary.Networking.M2Mqtt.Utility;
using uPLibrary.Networking.M2Mqtt.Exceptions;

using System;

using System.Threading.Tasks;
using System.Threading;

public class CubeAction : MonoBehaviour
{
    private MqttClient client;

    SynchronizationContext context;

    // MQTT接続先
    private string MQTT_IP_ADDRESS = "broker.shiftr.io";

    void Start()
    {
        // 接続先の指定
        client = new MqttClient(MQTT_IP_ADDRESS, 1883, false, null);

        // ユニークなID生成（重複すると通信が混乱する）
        string clientId = Guid.NewGuid().ToString();

        // 接続 shiftr.ioのUsername/Passwordも指定
        string username = "Username";
        string password = "Password";
        client.Connect(clientId, username, password);

        // 起動時のメッセージ送信
        client.Publish("/tjbot/oculus/message", System.Text.Encoding.UTF8.GetBytes("connect Oulus Quest!"), MqttMsgBase.QOS_LEVEL_AT_MOST_ONCE, false);
    }

    void Update()
    {
        if (OVRInput.GetDown(OVRInput.RawButton.A))
        {
            // AボタンでTJBotにアームが下がる命令が送られる
            // 一瞬赤くなる
            this.gameObject.GetComponent<Renderer>().material.color = Color.red;
            this.transform.localScale = new Vector3(0.6f, 0.6f, 0.6f);

            // MQTTへのPublish //////////////////////////////////////
            client.Publish("/tjbot/arm/down", System.Text.Encoding.UTF8.GetBytes("arm down"), MqttMsgBase.QOS_LEVEL_AT_MOST_ONCE, false);
        } else if (OVRInput.GetDown(OVRInput.RawButton.B)){
            // BボタンでTJBotにアームが下がる命令が送られる
            // 一瞬青くなる
            this.gameObject.GetComponent<Renderer>().material.color = Color.blue;
            this.transform.localScale = new Vector3(0.6f, 0.6f, 0.6f);

            // MQTTへのPublish //////////////////////////////////////
            client.Publish("/tjbot/arm/up", System.Text.Encoding.UTF8.GetBytes("arm up"), MqttMsgBase.QOS_LEVEL_AT_MOST_ONCE, false);
        } else {
            this.gameObject.GetComponent<Renderer>().material.color = Color.white;
            this.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
        }
    }

}