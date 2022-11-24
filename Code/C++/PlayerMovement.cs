using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public Rigidbody my_Rigidbody;

    void Start()
    {
        ball_Rigidbody.AddForce(-transform.forward * 2500f);
    }

    void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.name == "Cylinder") {
            print("You lose!")
        }
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        if (Input.GetKey("left") || Input.GetKey("right"))
        {
            Vector3 my_Input = new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical"));
            my_Rigidbody.MovePosition(transform.position + my_Input * Time.deltaTime * 5f);
        } 
    }
}
