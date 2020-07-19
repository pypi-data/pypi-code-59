# Copyright (c) 2020 Watsen Networks.  All Rights Reserved.

_M='Unrecognized member: '
_L='The top-level node-identifier must be prefixed by a namespace followed by a colon.'
_K='Parent data node ('
_J='Input document must contain at least one top-level node.'
_I='Data node ('
_H='Unrecognized schema path: '
_G='Invalid data path: '
_F=":admin-accounts'"
_E='[/] missing-data: expected'
_D='Validation failed: '
_C=') does not exist.'
_B=True
_A='/'
import re,sys,json,yangson,asyncio,aiohttp,traceback
from aiohttp import web,http_parser,streams
from multidict import CIMultiDict
from .dal import DataAccessLayer
class NodeAlreadyExists(Exception):0
class NodeNotFound(Exception):0
class ParentNodeNotFound(Exception):0
class InvalidDataPath(Exception):0
class InvalidInputDocument(Exception):0
class UnrecognizedInputNode(Exception):0
class UnrecognizedQueryParameter(Exception):0
class MissingQueryParameter(Exception):0
class NonexistentSchemaNode(Exception):0
class ValidationFailed(Exception):0
class ValidationLayer:
	def __init__(A,dm,dal):
		A.dm=dm;A.dal=dal;C=asyncio.get_event_loop();D=A.dal.handle_get_config_request(_A);E=C.run_until_complete(D);A.inst=A.dm.from_raw(E)
		try:A.inst.validate()
		except yangson.exceptions.SchemaError as B:assert str(B).startswith(_E);assert str(B).endswith(_F)
	async def reload(A):
		C=await A.dal.handle_get_config_request(_A);A.inst=A.dm.from_raw(C)
		try:A.inst.validate()
		except yangson.exceptions.SchemaError as B:assert str(B).startswith(_E);assert str(B).endswith(_F)
	async def handle_get_config_request(C,data_path,query_string):
		A=data_path;assert A!='';assert not(A!=_A and A[-1]==_A)
		try:D=C.dm.parse_resource_id(A)
		except yangson.exceptions.UnexpectedInput as B:raise InvalidDataPath(_G+str(B))
		except yangson.exceptions.NonexistentSchemaNode as B:raise NonexistentSchemaNode(_H+A)
		try:E=C.inst.goto(D)
		except yangson.exceptions.NonexistentInstance as B:raise NodeNotFound(_I+A+_C)
	async def handle_post_config_request(J,data_path,query_string,request_body):
		d='after';c='before';b='last';a='=';O=None;E=request_body;B=data_path;assert B!='';assert not(B!=_A and B[-1]==_A)
		if len(E)<1:raise InvalidInputDocument(_J)
		if len(E)>1:raise InvalidInputDocument('Input document must not have more than one top-level node.')
		try:T=J.dm.parse_resource_id(B)
		except yangson.exceptions.NonexistentSchemaNode as C:raise NonexistentSchemaNode('Unrecognized schema path for parent node: '+B)
		try:G=J.inst.goto(T)
		except yangson.exceptions.NonexistentInstance as C:raise ParentNodeNotFound(_K+B+_C)
		A=next(iter(E))
		if':'not in A:raise InvalidInputDocument(_L)
		U,H=A.split(':');L=G.schema_node;F=L.get_child(H,U)
		if F is O:raise UnrecognizedInputNode('Input document contains unrecognized top-level node.')
		if not L.ns is O:assert L.ns==F.ns
		if isinstance(F,yangson.schemanode.SequenceNode):
			if type(F)==yangson.schemanode.ListNode:
				V=F.keys[0];W=V[0]
				if type(E[A])!=list:raise InvalidInputDocument("Input node '"+H+"' not a 'list' node.")
				if len(E[A])!=1:raise InvalidInputDocument("Input 'list' node '"+H+"' must contain one element.")
				P=E[A][0];Q=P[W]
			elif type(F)==yangson.schemanode.LeafListNode:raise NotImplementedError('Inserting into LeafListNode not implemented yet.')
			else:raise AssertionError('Logic cannot reach this point')
			if B==_A:D=A;M=_A+D+a+Q
			else:D=H;M=B+_A+D+a+Q
			try:X=J.dm.parse_resource_id(M)
			except yangson.exceptions.NonexistentSchemaNode as C:raise NonexistentSchemaNode('Unrecognized schema path for insertion node: '+M)
			try:J.inst.goto(X)
			except yangson.exceptions.NonexistentInstance as C:pass
			else:raise NodeAlreadyExists('Child data node ('+M+') already exists.')
			try:K=G[D]
			except yangson.exceptions.NonexistentInstance:K=G.put_member(D,yangson.instvalue.ArrayValue([]))
			assert isinstance(K.schema_node,yangson.schemanode.SequenceNode);I=O
			if F.user_ordered:
				R=urllib.parse.parse_qs(query_string)
				try:I=R['insert']
				except KeyError:I=b
				else:
					if not any((I==A for A in('first',c,d,b))):raise UnrecognizedQueryParameter("Unrecognized 'input' query parameter value")
					if any((I==A for A in(c,d))):
						try:e=R['point']
						except KeyError:raise MissingQueryParameter("Missing 'point' query parameter, needed when 'insert' is '"+I+"'")
			assert I is O
			if len(K.value)==0:
				try:Y=K.update([P],raw=_B)
				except yangson.exceptions.RawMemberError as C:raise UnrecognizedInputNode('Incompatable node data. '+str(C))
				N=Y.up()
			else:Z=K[-1];N=Z.insert_after(P,raw=_B).up()
		else:
			if B==_A:D=A
			else:D=H
			if D in G:raise NodeAlreadyExists('Node "'+D+'" already exists.')
			try:
				if L.ns==O:N=G.put_member(A,E[A],raw=_B).up()
				else:N=G.put_member(H,E[A],raw=_B).up()
			except yangson.exceptions.RawMemberError as C:raise UnrecognizedInputNode(_M+str(C))
		S=N.top()
		try:S.validate()
		except Exception as C:raise ValidationFailed(_D+str(C))
		J.inst=S
	async def handle_put_config_request(C,data_path,query_string,request_body):
		D=request_body;B=data_path;assert B!='';assert not(B!=_A and B[-1]==_A)
		if len(D)<1:raise InvalidInputDocument(_J)
		G=next(iter(D))
		if':'not in G:raise InvalidInputDocument(_L)
		try:H=C.dm.parse_resource_id(B)
		except yangson.exceptions.UnexpectedInput as A:raise InvalidDataPath(_G+str(A))
		except yangson.exceptions.NonexistentSchemaNode as A:raise NonexistentSchemaNode(_H+B)
		try:E=C.inst.goto(H)
		except yangson.exceptions.NonexistentInstance as A:
			F=B.rsplit(_A,1)[0]
			if F=='':F=_A
			H=C.dm.parse_resource_id(F)
			try:E=C.inst.goto(H)
			except yangson.exceptions.NonexistentInstance as A:raise ParentNodeNotFound(_K+F+') does not exist. '+str(A))
			await C.handle_post_config_request(F,query_string,D);return
		try:
			if B==_A:I=E.update(D,raw=_B)
			elif isinstance(E.schema_node,yangson.schemanode.SequenceNode):I=E.update(D[G][0],raw=_B)
			else:I=E.update(D[G],raw=_B)
		except yangson.exceptions.RawMemberError as A:raise UnrecognizedInputNode(_M+str(A))
		except Exception as A:raise NotImplementedError(str(type(A))+' = '+str(A))
		J=I.top()
		try:J.validate()
		except Exception as A:raise ValidationFailed(_D+str(A))
		C.inst=J
	async def handle_delete_config_request(C,data_path):
		A=data_path;assert A!=''
		if A==_A:E=RootNode(ObjectValue({}),C.inst.schema_node,datetime.now())
		else:
			assert A[0]==_A;assert A[-1]!=_A
			try:J=C.dm.parse_resource_id(A)
			except yangson.exceptions.NonexistentSchemaNode as F:raise NonexistentSchemaNode('Unrecognized schema path for data node: '+A)
			try:D=C.inst.goto(J)
			except yangson.exceptions.NonexistentInstance as F:raise NodeNotFound(_I+A+_C)
			H=D.up()
			if type(D)==yangson.instance.ArrayEntry:
				B=H.delete_item(D.index)
				if len(B.value)==0:
					G=B.up()
					if isinstance(G.schema_node,yangson.schemanode.SequenceNode):I=G.delete_item(B.index);raise NotImplementedError('tested? list inside a list...')
					else:I=G.delete_item(B.name)
					B=I
			else:B=H.delete_item(D.name)
			E=B.top()
		try:E.validate()
		except Exception as F:raise ValidationFailed(_D+str(F))
		C.inst=E