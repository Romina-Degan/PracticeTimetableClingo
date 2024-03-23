/* eslint-disable prettier/prettier */
import React, { useState } from 'react';
import firestore from '@react-native-firebase/firestore';
import { useCurrentUserContext } from '../hooks/CurrentUserContext';
import userSpecifications from '../bhive-chores/instances/CBW.json';
import { firebase } from '@react-native-firebase/auth';

export function addToFirebaseStorage() {
    const { uid, profilePicURL, userName, currentHive, hiveName, hiveMembers } = useCurrentUserContext().values;
    var storageRef = firebase.storage().ref();
    var fileRef = storageRef.child(currentHive + ':' + userName);

    const userItems = JSON.stringify({ name: userName, userID: uid, hiveID: currentHive });
    var blob = new Blob([userItems], { type: 'json' });
    fileRef.put(blob).then(function (snapshot) {
        console.log('------')
        console.log('File written to Firestore');
    });
    console.log(userItems);
    try {
        fetch('/api/taskUser.py');
    } catch {
        console.log('Couldnt connect to API');
    }
    return userItems;
}
